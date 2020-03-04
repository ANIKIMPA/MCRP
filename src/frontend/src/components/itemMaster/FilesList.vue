<template>
  <div>
    <li @click="openModal">ITEM Files</li>
    <b-modal id="item-master-file-list" v-model="modalOpenned" title="Item Master Files" hide-footer>
      <p class="mb-2">Select ITEM File:</p>
      <b-list-group class="overflow-auto mh-300">
        <b-list-group-item button v-for="file in allItemMasterFiles" @click="openItemMaster(file)" :key="file.id" class="d-flex justify-content-between">
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
  name: "ItemMasterFilesList",
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
    ...mapActions(["fetchAllItemMasterFiles"]),
    ...mapMutations(["setItemMasterFile"]),
    openItemMaster(file) {
      this.$router.push({
        name: "item_master",
        params: {
          file: file.id
        }
      });
      this.setItemMasterFile(file);
      this.$bvModal.hide("item-master-file-list");
    },
    openModal() {
      this.modalOpenned = true;
      this.fetchAllItemMasterFiles();
    }
  },
  computed: {
    ...mapGetters(["allItemMasterFiles"])
  }
};
</script>

<style>
.mh-300 {
  max-height: 300px;
}
</style>