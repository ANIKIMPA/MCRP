<template>
  <b-modal
    size="lg"
    id="modal-parameters"
    title="MRP (MAST): Model Parameters"
    @ok.prevent="onSubmit"
  >
    <form>
      <div class="form-group row">
        <label class="col-form-label col-2" for="title">Title:</label>
        <div class="col-10">
          <input type="text" class="form-control" v-model="form.title" id="title" />
        </div>
      </div>

      <div class="form-group row">
        <!-- Numero de Items padres terminados -->
        <label class="col-form-label col-9" for="master_items">Number of Items Master Scheduled:</label>
        <div class="col-3">
          <input
            type="number"
            class="form-control"
            min="1"
            v-model="form.numberItems"
            :readonly="createFromBomFile"
            id="master_items"
          />
        </div>
      </div>
      <div class="form-group row">
        <!-- Número de master schedule items -->
        <label
          class="col-form-label col-9"
          for="planning_horizon_length"
        >Planning Horizon Length in Time Buckets:</label>
        <div class="col-3">
          <input
            type="number"
            class="form-control"
            v-model="form.planning_horizon_length"
            min="1"
            value="1"
            id="planning_horizon_length"
          />
        </div>
      </div>
      <div class="form-group row">
        <label
          class="col-form-label col-9"
          for="number_time_buckets"
        >Number of Time Buckets per Year:</label>
        <div class="col-3">
          <input
            type="number"
            class="form-control"
            v-model="form.number_time_buckets"
            min="1"
            value="1"
            id="number_time_buckets"
            readonly
          />
        </div>
      </div>
    </form>
  </b-modal>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "mastModelParameters",
  props: {
    createFromBomFile: Boolean
  },
  data() {
    return {
      form: {
        title: "Master Scheduled",
        planning_horizon_length: 0,
        number_time_buckets: 0,
        numberItems: 1
      }
    };
  },
  computed: {
    ...mapGetters(["mastFile", "getParentItems"])
  },
  mounted() {
    this.$root.$on("bv::modal::show", (bvEvent, modalId) => {
      if (modalId === "modal-parameters")
        if (this.createFromBomFile) {
          this.form.title = this.getParentItems[0].part_number;
          this.form.numberItems = this.getParentItems.length;
        } else {
          this.form.title = null;
          this.form.numberItems = 1;
        }
    });

    const unsubscribe = this.$store.subscribe(mutation => {
      if (mutation.type === "newMastFile") {
        let periods = "0";
        for (let num = 1; num < this.form.planning_horizon_length; num++) {
          periods += ",0";
        }
        // Add items to the file
        this.addMastItems({
          items_number: this.form.numberItems,
          part_numbers: this.getParentItems.map(item => item.part_number),
          createFromBomFile: this.createFromBomFile,
          periods: periods,
          file: this.mastFile.id
        });
      }

      // Redirect to datagrid page when data saved.
      if (mutation.type === "setMastItems") {
        this.$router.push({
          name: "master_schedule",
          params: {
            file: this.mastFile.id
          }
        });

        unsubscribe()
      }
    });
  },
  methods: {
    ...mapActions(["addMastItems", "createNewMastFile"]),
    onSubmit() {
      if (this.form.title && this.form.title.trim() != "") {
        this.createNewMastFile({
          title: this.form.title,
          number_of_items: this.getParentItems.length,
          planning_horizon_length: this.form.planning_horizon_length,
          number_time_buckets: this.form.number_time_buckets
        });

        this.$nextTick(() => {
          this.$bvModal.hide("modal-parameters");
        });
      }
    }
  }
};
</script>

<style></style>
