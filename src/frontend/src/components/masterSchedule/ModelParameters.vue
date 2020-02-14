<template>
  <b-modal size="lg" id="modal-multi-2" title="MRP (MAST): Model Parameters" @ok="onSubmit">
    <form>
      <div class="form-group row">
        <label class="col-form-label col-2" for="title">Title:</label>
        <div class="col-10">
          <input type="text" class="form-control" v-model="form.title" id="title" />
        </div>
      </div>

      <div class="form-group row">
		<!-- Numero de Items padres terminados -->
        <label class="col-form-label col-9" for="items_number">Number of Items Master Scheduled:</label>
        <div class="col-3">
          <input type="number" class="form-control" v-model="form.items_number" min="1" value="1" id="items_number" />
        </div>
      </div>
      <div class="form-group row">
		<!-- Número de periodos -->
        <label class="col-form-label col-9" for="planning_horizon_length" >Planning Horizon Length in Time Buckets:</label>
        <div class="col-3">
          <input type="number" class="form-control" v-model="form.planning_horizon_length" min="1" value="1" id="planning_horizon_length" />
        </div>
      </div>
      <div class="form-group row">
        <label class="col-form-label col-9" for="number_time_buckets" >Number of Time Buckets per Year:</label>
        <div class="col-3">
          <input type="number" class="form-control" v-model="form.number_time_buckets" min="1" value="1" id="number_time_buckets" />
        </div>
      </div>
    </form>
  </b-modal>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex";
export default {
  name: "mastModelParameters",
  data() {
    return {
      form: {
		title: "Master Scheduled",
		items_number: 1,
		planning_horizon_length: 0,
		number_time_buckets: 0
      }
    };
  },
  computed: {
    ...mapGetters(["getFirstFile", "fileSelected"]),
    ...mapState(["files"])
  },
  created() {
    this.$store.subscribe(mutation => {
      if (mutation.type === "newFile") {
        // Add items to the file
        for (let i = 1; i <= this.items_number; i++) {
          this.addItem({
            part_number: 100 * i,
            tipo: "MAT",
            parent: null,
            qty: 1,
            file: this.getFirstFile.id
          });
		}

        // Redirect to home page
        this.$router.push({
          name: "files",
          params: {
            file: this.getFirstFile.id
          }
		});
      }
	});
  },
  methods: {
    ...mapActions(["addItem", "createNewFile"]),
    onSubmit() {
      // Create new file
	//   this.createNewFile({ title: this.title, tipo: "Master Schedule" });
		console.log(this.form)
    }
  }
};
</script>

<style></style>
