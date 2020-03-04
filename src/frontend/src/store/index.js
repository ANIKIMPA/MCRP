import Vuex from "vuex";
import Vue from "vue";
import bomItems from "./modules/bom_items";
import bom_files from "./modules/bom_files";
import mast_files from "./modules/mast_files";
import periods from "./modules/periods";
import invFiles from "./modules/inv_files";
import invItems from "./modules/inv_items";
import itemMasterFiles from "./modules/item_master_files";
import itemsMasters from "./modules/items_masters";
import error from "./modules/error";

Vue.use(Vuex);

// Create store
export default new Vuex.Store({
  modules: {
    bomItems,
    mast_files,
    bom_files,
    periods,
    invFiles,
    invItems,
    itemMasterFiles,
    itemsMasters,
    error
  }
});