<template>
  <div>
    <li @click="openModal">BOM Files</li>
    <b-modal id="bom-file-list" v-model="modalOpenned" title="Bill of Material Files" hide-footer>
      <p class="mb-2">Select BOM File:</p>
      <b-list-group class="overflow-auto mh-300">
        <b-list-group-item button v-for="file in allBomFiles" @click="openBom(file)" :key="file.id" class="d-flex justify-content-between">
			<span><i class="far fa-file-alt"></i> {{ file.title }}</span> <small style="font-style: italic;">{{ file.created_date | formatDate }}</small>
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
    ...mapActions(["fetchAllBomFiles"]),
    ...mapMutations(["setBomFile"]),
    openBom(file) {
      this.$router.push({
        name: "bill_of_material",
        params: {
          file: file.id
        }
      });
      this.setBomFile(file);
      this.$bvModal.hide("bom-file-list");
    },
    openModal() {
      this.modalOpenned = true;
      this.fetchAllBomFiles();
    }
  },
  computed: {
    ...mapGetters(["allBomFiles"])
  }
};
</script>

<style>
.mh-300 {
  max-height: 300px;
}
</style>