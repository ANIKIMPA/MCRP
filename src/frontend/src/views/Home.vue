<template>
	<b-container class="bv-example-row bv-example-row-flex-cols">

		<b-row align-v="center" class="h-200">
			<b-col>
				<h1>Welcome to Storm 5.0</h1>
			</b-col>
		</b-row>
	</b-container>
</template>

<script>
export default {
	name: "home",
	// onIdle() {
	// 	this.$bvToast.toast("Tamo onIdle", {
    //     title: 'Probando',
    //     variant: "info",
    //     solid: true,
    //     autoHideDelay: 5000,
    //   })
	// },
	// onActive() {
	// 	this.$bvToast.toast("Tamo onActive", {
    //     title: 'Probando',
    //     variant: "info",
    //     solid: true,
    //     autoHideDelay: 5000,
    //   })
	// }
};
</script>

<style scoped>
.h-200 {
	height: 200px;
}
</style>
