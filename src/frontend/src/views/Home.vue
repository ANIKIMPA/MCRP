<template>
	<b-container class="bv-example-row bv-example-row-flex-cols">

		<b-row align-v="center" class="h-200">
			<b-col>
				<h1>Welcome to Storm 5.0</h1>
			</b-col>
			<h2>{{ file }}</h2>
		</b-row>
	</b-container>
</template>

<script>
export default {
	name: "home",
	data() {
		return {};
	},
	components: {},
	computed: {
		file() {
			return this.$store.state.fileSelected.name;
		}
	}
};
</script>

<style scoped>
.h-200 {
	height: 200px;
}
</style>
