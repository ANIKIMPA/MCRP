<template>
	<div>
		<button @click="onSubmit">Click</button>
	</div>
</template>

<script>
import { mapActions } from 'vuex';
export default {
	methods: {
    ...mapActions(["fetchMastersSchedules"]),
		onSubmit() {
			this.$router.push({
				name: "master_schedule",
				params: {
					numberOfPeriods: 7
				}
			});
		}
  },
	created() {
    this.fetchMastersSchedules(6)
  }
};
</script>

<style>
</style>
