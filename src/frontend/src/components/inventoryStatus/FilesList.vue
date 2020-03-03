<template>
  <div>
    <li @click="openModal">INV Files</li>
    <b-modal id="inv-file-list" v-model="modalOpenned" title="Inventory Status Files" hide-footer>
      <p class="mb-2">Select INV File:</p>
      <b-list-group class="overflow-auto mh-300">
        <b-list-group-item button v-for="file in allInvFiles" @click="openInv(file)" :key="file.id" class="d-flex justify-content-between">
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
  name: "InvFilesList",
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
    ...mapActions(["fetchAllInvFiles"]),
    ...mapMutations(["setInvFile"]),
    openInv(file) {
      this.$router.push({
        name: "inventory_status",
        params: {
          file: file.id
        }
      });
      this.setInvFile(file);
      this.$bvModal.hide("inv-file-list");
    },
    openModal() {
      this.modalOpenned = true;
      this.fetchAllInvFiles();
    }
  },
  computed: {
    ...mapGetters(["allInvFiles"])
  }
};
</script>

<style>
.mh-300 {
  max-height: 300px;
}
</style>