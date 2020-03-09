<template>
  <div>
    <li @click="openModal">MAST Files</li>
    <b-modal id="mast-file-list" v-model="modalOpenned" title="Master Schedule Files" hide-footer>
      <p class="mb-2">Select MAST File:</p>
      <b-list-group class="overflow-auto mh-300">
        <b-list-group-item
          button
          v-for="file in allMastFiles"
          @click="openMast(file)"
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
import { mapActions, mapGetters, mapMutations } from "vuex";
import moment from "moment";
export default {
  name: "MastfileList",
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
    ...mapActions(["fetchAllMastFiles", "deleteMastFile"]),
    ...mapMutations(["setMastFile"]),
    openMast(file) {
      this.$router.push({
        name: "master_schedule",
        params: {
          file: file.id
        }
      });
      this.$bvModal.hide("mast-file-list");
    },
    openModal() {
      this.modalOpenned = true;
      this.fetchAllMastFiles();
    },
    deleteFile(file) {
      if (this.mastFile.id === file.id) {
        this.$router.push("/");
      }
      file.removed = true;
      this.deleteMastFile(file);
    }
  },
  computed: {
    ...mapGetters(["allMastFiles", "mastFile"])
  }
};
</script>

<style scoped>
.mh-300 {
  max-height: 300px;
}
</style>