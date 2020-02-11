import Vuex from 'vuex';
import Vue from 'vue';
import items from './modules/items';
import files from './modules/files';

Vue.use(Vuex);

// Create store
export default new Vuex.Store({
    modules: {
        items,
        files,
    }
})