import xlwt

from django.http import HttpResponse
from users.models import Usuario
from mrp.models import BomItem, MastItem, InvItem, ItemMaster

def export_report_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="report.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Report')
    ws.col(2).width = 200 * 20
    ws.col(3).width = 256 * 20
    ws.col(4).width = 120 * 20
    ws.col(5).width = 220 * 20
    ws.col(6).width = 256 * 20

    for count in range(0, 62):
        ws.row(count).height_mismatch = True
        ws.row(count).height = 320

    # Create Custom color for cells
    xlwt.add_palette_colour("custom_colour", 0x21)
    wb.set_colour_RGB(0x21, 211, 247, 253)
    th_style = xlwt.easyxf('pattern: pattern solid, fore_color custom_colour; border: top thick, right thick, bottom thick, left thick; font: bold 1; align: vert centre, horiz center;')
    td_style = xlwt.easyxf('border: top thick, right thick, bottom thick, left thick; font: bold 1; align: vert centre, horiz center')

    bomItems = BomItem.objects.filter(file=3)
    mastItems = MastItem.objects.filter(file=3)
    invItems = InvItem.objects.filter(file=1)
    itemsMasters = ItemMaster.objects.filter(file=1)

    current_table = 2
    for idx, bomItem in enumerate(bomItems):
        ws.write(current_table + 0, 2, 'Item Number', th_style)
        ws.write(current_table + 0, 3, bomItem.part_number, td_style)
        ws.write(current_table + 0, 5, 'Yield (%)', th_style)
        ws.write(current_table + 0, 6, itemsMasters[idx].yield_percent, td_style)

        ws.write(current_table + 2, 2, 'Lead Time', th_style)
        ws.write(current_table + 2, 3, itemsMasters[idx].lead_time, td_style)
        ws.write(current_table + 2, 5, 'Order Cost', th_style)
        ws.write(current_table + 2, 6, itemsMasters[idx].order_cost, td_style)

        ws.write(current_table + 4, 2, 'Parent', th_style)
        ws.write(current_table + 4, 3, bomItem.parent, td_style)
        ws.write(current_table + 4, 5, 'Carrying Cost', th_style)
        ws.write(current_table + 4, 6, itemsMasters[idx].carrying_cost, td_style)
        
        ws.write(current_table + 6, 2, 'Quantity', th_style)
        ws.write(current_table + 6, 3, bomItem.qty, td_style)
        ws.write(current_table + 6, 5, 'Lot Size', th_style)
        ws.write(current_table + 6, 6, itemsMasters[idx].lot_size, td_style)

        ws.write(current_table + 7, 5, 'Factor', th_style)
        ws.write(current_table + 7, 4, '')

        ws.write(current_table + 8, 2, 'Safety Stock', th_style)
        ws.write(current_table + 8, 3, invItems[idx].safe_stock, td_style)
        
        ws.write(current_table + 9, 5, 'On Hand', th_style)

        ws.write(current_table + 10, 2, 'Period', th_style)
        ws.write(current_table + 10, 3, 'Gross Requirement', th_style)
        ws.write(current_table + 10, 4, 'Receipts', th_style)
        ws.write(current_table + 10, 5, invItems[idx].on_hand, td_style)
        ws.write(current_table + 10, 6, 'Net Requirement', th_style)
        
        if idx < len(mastItems):
            for i, period in enumerate(mastItems[idx].periods.split(",")):
                ws.write(current_table + i + 11, 2, i, td_style)
                ws.write(current_table + i + 11, 3, int(period), td_style)

        current_table += 25

    wb.save(response)
    return response


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['First name', 'Last name', 'Email address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Usuario.objects.all().values_list('first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
    

def export_styling_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Styling Data') # this will make a sheet named Users Data - First Sheet
    xlwt.add_palette_colour("custom_colour", 0x21)
    wb.set_colour_RGB(0x21, 211, 247, 253)

    styles = dict(
        bold = 'font: bold 1',
        italic = 'font: italic 1',
        # Wrap text in the cell
        wrap_bold = 'font: bold 1; align: wrap 1;',
        # White text on a blue background
        reversed = 'pattern: pattern solid, fore_color blue; font: color white;',
        # Light orange checkered background
        light_orange_bg = 'pattern: pattern fine_dots, fore_color white, back_color orange;',
        # Heavy borders
        bordered = 'border: top thick, right thick, bottom thick, left thick;',
        # 16 pt red text
        big_red = 'font: height 320, color red;',

        custom_color = 'pattern: pattern solid, fore_color custom_colour;',
    )

    for idx, k in enumerate(sorted(styles)):
        style = xlwt.easyxf(styles[k])
        ws.write(idx, 0, k)
        ws.write(idx, 1, styles[k], style)

    wb.save(response)

    return response