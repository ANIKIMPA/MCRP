import Vuex from "vuex";
import Vue from "vue";
import user from "./modules/user";
import bomItems from "./modules/bom_items";
import bom_files from "./modules/bom_files";
import mast_files from "./modules/mast_files";
import mastItems from "./modules/mast_items";
import invFiles from "./modules/inv_files";
import invItems from "./modules/inv_items";
import itemMasterFiles from "./modules/item_master_files";
import itemsMasters from "./modules/items_masters";
import token from "./modules/token";
import error from "./modules/error";

Vue.use(Vuex);

// Create store
export default new Vuex.Store({
  modules: {
    user,
    bomItems,
    mast_files,
    bom_files,
    mastItems,
    invFiles,
    invItems,
    itemMasterFiles,
    itemsMasters,
    token,
    error
  }
});