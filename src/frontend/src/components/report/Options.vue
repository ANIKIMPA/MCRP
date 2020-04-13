<template>
  <div>
    <b-modal id="report-options" size="lg" title="MRP : Report Options">
      <b-row class="px-2 pb-3">
        <div class="w-100">
          <b-form-checkbox
            v-model="checkBox.explosionReport"
            :value="true"
            :unchecked-value="false"
          >Explosion Report</b-form-checkbox>
        </div>
        <b-col>
          <b-form-radio
            v-model="radio.allItems"
            :value="false"
            :disabled="!checkBox.explosionReport"
          >Exclude items with no activity</b-form-radio>
          <b-form-radio
            v-model="radio.allItems"
            :value="true"
            :disabled="!checkBox.explosionReport"
          >All</b-form-radio>
        </b-col>
      </b-row>
      <b-row class="px-2 py-3 border-top border-bottom">
        <b-col cols="6">
          <b-row>
            <b-form-checkbox
              v-model="checkBox.indentedBom"
              :value="true"
              :unchecked-value="false"
            >Indented Bill of Material Report</b-form-checkbox>
          </b-row>
          <b-row>
            <b-col>
              <b-form-radio :value="false" :disabled="!checkBox.indentedBom">By Level</b-form-radio>
              <b-form-radio :value="true" :disabled="!checkBox.indentedBom">Single Item</b-form-radio>
            </b-col>
            <b-col>
              <b-form-radio :value="false" :disabled="!checkBox.indentedBom">All Levels</b-form-radio>
              <b-form-radio :value="true" :disabled="!checkBox.indentedBom">Single Level</b-form-radio>
            </b-col>
          </b-row>
        </b-col>
        <b-col cols="6">
          <b-form-select :options="options" multiple :select-size="3"></b-form-select>
        </b-col>
      </b-row>
      <b-row class="px-2 pt-3">
        <b-col cols="6">
          <b-row>
            <b-form-checkbox
              v-model="checkBox.whereUsedReport"
              :value="true"
              :unchecked-value="false"
            >Where-Used Report</b-form-checkbox>
          </b-row>
          <b-row>
            <b-col>
              <b-form-radio :value="false" :disabled="!checkBox.whereUsedReport">By Level</b-form-radio>
              <b-form-radio :value="true" :disabled="!checkBox.whereUsedReport">Single Item</b-form-radio>
            </b-col>
            <b-col>
              <b-form-radio :value="false" :disabled="!checkBox.whereUsedReport">All Levels</b-form-radio>
              <b-form-radio :value="true" :disabled="!checkBox.whereUsedReport">Single Level</b-form-radio>
            </b-col>
          </b-row>
        </b-col>

        <b-col cols="6">
          <b-form-select :options="options" multiple :select-size="4"></b-form-select>
        </b-col>
      </b-row>

      <template v-slot:modal-footer>
        <div class="w-100 text-center">
          <b-button variant="secondary" class="mx-3 w-10" @click="openFinalReport" :disabled="!checkBox.explosionReport">Ok</b-button>
          <b-button
            variant="secondary"
            class="mx-3 w-10"
            @click="$bvModal.hide('report-options')"
          >Cancel</b-button>
        </div>
      </template>
    </b-modal>
  </div>
</template>

<script>
export default {
  name: "ReportOptions",
  data() {
    return {
      options: [
        { value: "a", text: "This is First option" },
        { value: "b", text: "Default Selected Option" },
        { value: "c", text: "This is another option" },
        { value: "d", text: "This one is disabled" },
        { value: "e", text: "This is option e" },
        { value: "f", text: "This is option f" },
        { value: "g", text: "This is option g" }
      ],
      checkBox: {
        explosionReport: true,
        indentedBom: false,
        whereUsedReport: false
      },
      radio: {
        allItems: true
      }
    };
  },
  methods: {
    openFinalReport() {
      this.$router.push({
        name: "final_report"
      });
      this.$bvModal.hide('report-options')
    }
  }
};
</script>

<style>
</style>