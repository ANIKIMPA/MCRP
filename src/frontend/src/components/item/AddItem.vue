<template>
    <b-container>
        <h3>Add Item</h3>

        <b-form @submit="onSubmit">
            <b-form-group label="Part Number" label-for="part_number">
                <b-form-input id="part_number" v-model="form.part_number" type="text" placeholder="Enter part number"/>
            </b-form-group>

            <b-form-group label="Type" label-for="tipo">
                <b-form-input id="tipo" v-model="form.tipo" placeholder="Enter type"/>
            </b-form-group>

            <b-form-group label="Parent:" label-for="parent">
                <b-form-select id="parent" v-model="form.parent">
					<b-form-select-option v-for="item in getAllItems" :key="item.id" :value="item.id">{{ item.part_number }}</b-form-select-option>
				</b-form-select>
            </b-form-group>

            <b-form-group label="Qty:" label-for="qty">
                <b-form-input id="qty" min="1" type="number" v-model="form.qty" placeholder="Enter qty"/>
            </b-form-group>

            <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </b-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
    name: "AddItem",
    data() {
        return {
			form: { part_number: "", tipo: "", parent: null, qty: 1 },
		}
	},
	computed: mapGetters(['getAllItems']),
	methods: {
		...mapActions(["addItem"]),
		onSubmit(e) {
			e.preventDefault();
			
			this.addItem(this.form)
		}
	}
};
</script>

<style></style>
