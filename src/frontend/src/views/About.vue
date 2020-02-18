<template>
  <div>
		<form @submit="onSubmit">
			<div class="form-group">
				<label for="part_number">Part Number</label>
				<input type="text" id="part_number" v-model="form.part_number">
			</div>
			<div class="form-group">
				<label for="period">Period</label>
				<input type="text" id="period" v-model="form.period">
			</div>
			<div class="form-group">
				<label for="order">Order</label>
				<input type="text" id="order" v-model="form.order">
			</div>

			<button type="submit">Submit</button>
		</form>
			<button @click="check">Check</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
			id: 1,
			form: {
				id: Number,
				part_number: "",
				order: "",
				file: 6
			},
      masters_schedules: []
    };
  },
  methods: {
    onSubmit(e) {
			e.preventDefault();
			this.form.id = this.id;

			let idx = this.masters_schedules.findIndex((mast) => mast.part_number == this.form.part_number)

			if (idx >= 0) {
				this.masters_schedules[idx][`period${this.form.order}`] = null;
			} else {
				this.form[`period${this.form.order}`] = null
				this.masters_schedules.push({...this.form});
			}
			
			this.id++
		},
		check() {
			console.log(this.masters_schedules)
		}
  }
};
</script>

<style>
</style>
