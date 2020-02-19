import Vuex from "vuex";
import Vue from "vue";
import items from "./modules/items";
import bom_files from "./modules/bom_files";
import mast_files from "./modules/mast_files";
import periods from "./modules/periods";

Vue.use(Vuex);

// Create store
export default new Vuex.Store({
  modules: {
    items,
    mast_files,
    bom_files,
    periods
  }
});