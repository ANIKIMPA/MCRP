import Vuex from "vuex";
import Vue from "vue";
import items from "./modules/items";
import files from "./modules/files";
import masters_schedules from "./modules/masters_schedules";

Vue.use(Vuex);

// Create store
export default new Vuex.Store({
  modules: {
    items,
    files,
    masters_schedules
  }
});
