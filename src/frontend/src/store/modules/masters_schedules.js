import axios from "axios";

const state = {
  masters_schedules: [
    { part_number: "600", period: null, order: 1, file_id: 22 },
    { part_number: "600", period: null, order: 2, file_id: 22 },
    { part_number: "600", period: null, order: 3, file_id: 22 },
    { part_number: "600", period: null, order: 4, file_id: 22 },
    { part_number: "600", period: null, order: 5, file_id: 22 },
    { part_number: "600", period: null, order: 6, file_id: 22 },
    { part_number: "600", period: null, order: 7, file_id: 22 },
    { part_number: "700", period: null, order: 1, file_id: 22 },
    { part_number: "700", period: null, order: 2, file_id: 22 },
    { part_number: "700", period: null, order: 3, file_id: 22 },
    { part_number: "700", period: null, order: 4, file_id: 22 },
    { part_number: "700", period: null, order: 5, file_id: 22 },
    { part_number: "700", period: null, order: 6, file_id: 22 },
    { part_number: "700", period: null, order: 7, file_id: 22 },
    { part_number: "bin", period: null, order: 1, file_id: 22 },
    { part_number: "bin", period: null, order: 2, file_id: 22 },
    { part_number: "bin", period: null, order: 3, file_id: 22 },
    { part_number: "bin", period: null, order: 4, file_id: 22 },
    { part_number: "bin", period: null, order: 5, file_id: 22 },
    { part_number: "bin", period: null, order: 6, file_id: 22 },
    { part_number: "bin", period: null, order: 7, file_id: 22 },
    { part_number: "fhdjg", period: null, order: 1, file_id: 22 },
    { part_number: "fhdjg", period: null, order: 2, file_id: 22 },
    { part_number: "fhdjg", period: null, order: 3, file_id: 22 },
    { part_number: "fhdjg", period: null, order: 4, file_id: 22 },
    { part_number: "fhdjg", period: null, order: 5, file_id: 22 },
    { part_number: "fhdjg", period: null, order: 6, file_id: 22 },
    { part_number: "fhdjg", period: null, order: 7, file_id: 22 },
  ]
};

const getters = {
  getAllMastersSchedules: state => state.masters_schedules
};

const actions = {
  // Obtener lista de masters_schedules
  async fetchMastersSchedules({ commit }, file_id) {
    await axios
      .get(
        `http://localhost:8000/api/v1.0/mrp/files/${file_id}/masters-schedules`
      )
      .then(response => {
        commit("updateMastersSchedules", response.data);
      })
      .catch(error => {
        console.log(error);
      });
  },
  // Agregar master_schedule
  addMasterSchedule({ commit }, master_schedule) {
    axios.post("http://localhost:8000/api/v1.0/mrp/masters-schedules/", master_schedule)
      .then(response => {
        commit("newMasterSchedule", response.data);
      })
      .catch(error => {
        console.log(error);
      });
  },

  async updateMasterSchedule({ commit }, master_schedule) {
    await axios
      .put(
        `http://localhost:8000/api/v1.0/mrp/masters-schedules/${master_schedule.id}/`,
        master_schedule
      )
      .then(response => {
        commit("updateMasterSchedule", response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }
};

const mutations = {
  // Set all masters_schedules to state
  updateMastersSchedules: (state, masters_schedules) =>
    (state.masters_schedules = masters_schedules),

  //Add master_schedule to state
  newMasterSchedule: (state, master_schedule) =>
    state.masters_schedules.push(master_schedule),

  // Update master_schedule in state
  updateMasterSchedule: (state, updMasterSchedule) => {
    const index = state.masters_schedules.findIndex(
      master_schedule => master_schedule.id === updMasterSchedule.id
    );
    if (index !== -1) {
      state.masters_schedules.splice(index, 1, updMasterSchedule);
    }
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
