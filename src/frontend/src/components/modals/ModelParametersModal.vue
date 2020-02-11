<template>
  <b-modal
    size="lg"
    id="modal-multi-2"
    title="MRP (BOM): Model Parameters"
    @ok="GoHome"
  >
    <div class="form-group row">
      <label class="col-form-label col-2" for="title">Title:</label>
      <div class="col-10">
        <input type="text" class="form-control" v-model="title" id="title" />
      </div>
    </div>
    <div class="form-group row">
      <label class="col-form-label col-9" for="items_number"
        >Total Number of Items in the File</label
      >
      <div class="col-3">
        <input
          type="number"
          class="form-control"
          v-model="items_number"
          min="1"
          value="1"
          id="items_number"
        />
      </div>
    </div>
  </b-modal>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex";
export default {
  props: ["tipo"],
  data() {
    return {
      title: "",
      items_number: 1
    };
  },
  computed: {
    ...mapGetters(["getFirstFile"]),
    ...mapState(["files"])
  },
  created() {
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === 'newFile') {
        console.log(`newFile to ${state.files}`);
        
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
          name: "home",
          params: {
            title: this.title,
            items_number: this.items_number
          }
        });
      }
    });
  },
  methods: {
    ...mapActions(["addItem", "createNewFile"]),
    GoHome() {
      // Create new file
      this.createNewFile({ title: this.title, tipo: this.tipo });
    }
  }
};
</script>

<style></style>
