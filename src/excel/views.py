import xlwt

from django.http import HttpResponse
from users.models import Usuario
from mrp.models import Report, ReportItem, ReportPeriod
from decimal import Decimal
from .functions import dollarFormat

def export_report_xls(request, report_id):
    report = Report.objects.get(pk=report_id)
    items = ReportItem.objects.filter(report=report_id)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{report.title}.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Report')
    COLS_WIDTH = 256 * 20
    ws.col(2).width = COLS_WIDTH
    ws.col(3).width = COLS_WIDTH
    ws.col(4).width = COLS_WIDTH
    ws.col(5).width = COLS_WIDTH
    ws.col(6).width = COLS_WIDTH

    for count in range(0, 62):
        ws.row(count).height_mismatch = True
        ws.row(count).height = 320

    # Create Custom color for cells
    xlwt.add_palette_colour("custom_colour", 0x21)
    wb.set_colour_RGB(0x21, 211, 247, 253)
    th_style = xlwt.easyxf('pattern: pattern solid, fore_color custom_colour; border: top thin, right thin, bottom thin, left thin; font: bold 1; align: vert centre, horiz center;')
    td_style = xlwt.easyxf('border: top thin, right thin, bottom thin, left thin; font: bold 1; align: vert centre, horiz center')

    current_table = 2
    total_carrying_cost = 0
    total_order_cost = 0

    for item in items:
        ws.write(current_table + 0, 2, 'Item Number', th_style)
        ws.write(current_table + 0, 3, item.part_number, td_style)
        ws.write(current_table + 0, 5, 'Yield (%)', th_style)
        ws.write(current_table + 0, 6, item.yield_percent, td_style)

        ws.write(current_table + 2, 2, 'Lead Time', th_style)
        ws.write(current_table + 2, 3, item.lead_time, td_style)
        ws.write(current_table + 2, 5, 'Order Cost', th_style)
        ws.write(current_table + 2, 6, item.order_cost, td_style)

        ws.write(current_table + 4, 2, 'Parent', th_style)
        ws.write(current_table + 4, 3, item.parent, td_style)
        ws.write(current_table + 4, 5, 'Carrying Cost', th_style)
        ws.write(current_table + 4, 6, item.carrying_cost, td_style)
        
        ws.write(current_table + 6, 2, 'Quantity', th_style)
        ws.write(current_table + 6, 3, item.qty, td_style)
        ws.write(current_table + 6, 5, 'Lot Size', th_style)
        ws.write(current_table + 6, 6, item.lot_size, td_style)

        ws.write(current_table + 7, 5, 'Factor', th_style)
        ws.write(current_table + 7, 4, '')

        ws.write(current_table + 8, 2, 'Safety Stock', th_style)
        ws.write(current_table + 8, 3, item.safe_stock, td_style)
        
        ws.write(current_table + 9, 5, 'On Hand', th_style)

        ws.write(current_table + 10, 2, 'Period', th_style)
        ws.write(current_table + 10, 3, 'Gross Requirement', th_style)
        ws.write(current_table + 10, 4, 'Receipts', th_style)
        ws.write(current_table + 10, 5, item.on_hand, td_style)
        ws.write(current_table + 10, 6, 'Net Requirement', th_style)

        periods = ReportPeriod.objects.filter(item=item.id)
        total_inventory = 0
        net_req_count = 0

        for period in periods:
            row = period.period - 1
            ws.write(current_table + row + 11, 2, period.period, td_style)
            ws.write(current_table + row + 11, 3, period.gross_requirement, td_style)
            ws.write(current_table + row + 11, 4, period.receipt, td_style)
            ws.write(current_table + row + 11, 5, period.on_hand, td_style)
            ws.write(current_table + row + 11, 6, period.net_requirement, td_style)

            if period.on_hand > 0:
                total_inventory += period.on_hand
            if period.net_requirement > 0: net_req_count += 1

        average_inventory = total_inventory / len(periods)
        carrying_cost = Decimal(average_inventory) * item.carrying_cost
        order_cost = net_req_count * item.order_cost
        total_cost = carrying_cost + order_cost

        ws.write(current_table + row + 12, 2, "Total Inventory", th_style)
        ws.write(current_table + row + 12, 3, "Average Inventory", th_style)
        ws.write(current_table + row + 12, 4, "Carrying Cost", th_style)
        ws.write(current_table + row + 12, 5, "Order Cost", th_style)
        ws.write(current_table + row + 12, 6, "Total Cost", th_style)
        ws.write(current_table + row + 13, 2, total_inventory, td_style)
        ws.write(current_table + row + 13, 3, average_inventory, td_style)
        ws.write(current_table + row + 13, 4, dollarFormat(carrying_cost), td_style)
        ws.write(current_table + row + 13, 5, dollarFormat(order_cost), td_style)
        ws.write(current_table + row + 13, 6, dollarFormat(total_cost), td_style)

        total_carrying_cost += carrying_cost
        total_order_cost += order_cost
        current_table += 25

    final_total_cost = total_carrying_cost +  total_order_cost
    ws.write(current_table + row - 9, 4, "Total Carrying Cost", th_style)
    ws.write(current_table + row - 9, 5, "Total Order Cost", th_style)
    ws.write(current_table + row - 9, 6, "Total Cost", th_style)
    ws.write(current_table + row - 8, 4, dollarFormat(total_carrying_cost), td_style)
    ws.write(current_table + row - 8, 5, dollarFormat(total_order_cost), td_style)
    ws.write(current_table + row - 8, 6, dollarFormat(final_total_cost), td_style)

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
        bordered = 'border: top thin, right thin, bottom thin, left thin;',
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