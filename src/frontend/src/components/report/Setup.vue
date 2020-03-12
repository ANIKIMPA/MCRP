<template>
  <div>
    <li class="parent" @click.prevent="openModal">
      <a href="#">Report</a>
    </li>
    <b-modal id="report-setup" size="xl" v-model="modalOpenned" title="MRP : Filename Setup">
      <table class="w-100">
        <tr>
          <td width="20%" class="text-left">Bill of Material:</td>
          <td width="66%" class="text-center">
            <input type="text" class="form-control" v-model="files.billOfMaterial" readonly />
          </td>
          <td width="14%" class="text-right">
            <SelectBomFile :createFromBomFile="true" />
          </td>
        </tr>
        <tr>
          <td class="text-left">Master Schedule:</td>
          <td class="text-center">
            <input type="text" class="form-control" v-model="files.masterSchedule" readonly />
          </td>
          <td class="text-right">
            <SelectMastFile />
          </td>
        </tr>
        <tr>
          <td class="text-left">Inventory Status:</td>
          <td class="text-center">
            <input type="text" class="form-control" v-model="files.inventoryStatus" readonly />
          </td>
          <td class="text-right">
            <SelectInvFile />
          </td>
        </tr>
        <tr>
          <td class="text-left">Item Master:</td>
          <td class="text-center">
            <input type="text" class="form-control" v-model="files.itemMaster" readonly />
          </td>
          <td class="text-right">
            <SelectItemFile />
          </td>
        </tr>
      </table>

      <template v-slot:modal-footer>
        <div class="w-100 text-center">
          <div>*Note*: Reports are generated from the last saved versions of the above files.</div>
          <b-button variant="secondary" class="mx-3" @click="showSetupOptionsModal">Report</b-button>
          <b-button variant="secondary" class="mx-3" @click="modalOpenned=false">Cancel</b-button>
        </div>
      </template>
    </b-modal>

    <ReportOptions/>
  </div>
</template>

<script>
import SelectBomFile from "@/components/billOfMaterial/SelectBomFile";
import SelectMastFile from "@/components/masterSchedule/SelectMastFile";
import SelectInvFile from "@/components/inventoryStatus/SelectInvFile";
import SelectItemFile from "@/components/itemMaster/SelectItemFile";
import ReportOptions from "./Options"
import { mapGetters } from "vuex";
export default {
  name: "ReportSetup",
  components: {
    SelectBomFile,
    SelectMastFile,
    SelectInvFile,
    SelectItemFile,
    ReportOptions
  },
  data() {
    return {
      modalOpenned: false,
      files: {
        billOfMaterial: "",
        masterSchedule: "",
        inventoryStatus: "",
        itemMaster: ""
      }
    };
  },
  methods: {
    openModal() {
      this.modalOpenned = true;
    },
    showSetupOptionsModal() {
      this.$bvModal.show('report-options');
      this.modalOpenned = false;
    }
  },
  watch: {
    bomFile() {
      this.files.billOfMaterial = this.bomFile.title;
    },
    mastFile() {
      this.files.masterSchedule = this.mastFile.title;
    },
    invFile() {
      this.files.inventoryStatus = this.invFile.title;
    },
    itemMasterFile() {
      this.files.itemMaster = this.itemMasterFile.title;
    }
  },
  computed: {
    ...mapGetters(["bomFile", "mastFile", "invFile", "itemMasterFile"])
  }
};
</script>
<style>
td {
  padding-top: 6px;
  padding-bottom: 6px;
}
</style>