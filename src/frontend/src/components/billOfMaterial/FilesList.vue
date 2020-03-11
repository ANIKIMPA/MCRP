<template>
  <div>
    <li @click="openModal">BOM Files</li>
    <b-modal id="bom-file-list" v-model="modalOpenned" title="Bill of Material Files" hide-footer>
      <p class="mb-2">Select BOM File:</p>
      <b-list-group class="overflow-auto mh-300">
        <b-list-group-item
          button
          v-for="file in allBomFiles"
          @click="openBom(file)"
          :key="file.id"
          class="d-flex justify-content-between"
        >
          <span style="width: 50%">
            <i class="fas fa-file-alt"></i>
            {{ file.title }}
          </span>
          <small style="font-style: italic;">{{ file.created_date | formatDate }}</small>
          <a
            href="#"
            @click.stop.prevent="deleteFile(file)"
            class="text-danger px-1"
            style="text-align:right;"
          >
            <i class="fas fa-trash-alt"></i>
          </a>
        </b-list-group-item>
      </b-list-group>
    </b-modal>
  </div>
</template>

<script>
import moment from "moment";
import { mapActions, mapGetters, mapMutations } from "vuex";
export default {
  name: "BomfileList",
  data() {
    return {
      modalOpenned: false
    };
  },
  filters: {
    formatDate(value) {
      return moment(value).format("L") + " " + moment(value).format("hh:mma");
    }
  },
  methods: {
    ...mapActions(["fetchAllBomFiles", "deleteBomFile"]),
    ...mapMutations(["setBomFile"]),
    openBom(file) {
      this.$router.push({
        name: "bill_of_material",
        params: {
          file: file.id
        }
      });
      this.$bvModal.hide("bom-file-list");
    },
    openModal() {
      this.modalOpenned = true;
      this.fetchAllBomFiles();
    },
    deleteFile(file) {
			if (this.bomFile.id === file.id) {
				this.$router.push("/");
			}
      file.removed = true;
      this.deleteBomFile(file);
    }
  },
  computed: {
    ...mapGetters(["allBomFiles", "bomFile"])
  }
};
</script>

<style>
.mh-300 {
  max-height: 300px;
}
</style>