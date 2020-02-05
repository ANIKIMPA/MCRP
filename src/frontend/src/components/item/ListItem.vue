<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado de Items</h2>

                <div class="col-md-12">
                    <b-table striped hover :items="items" :fields="fields">

                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            items: []
        }
    },
    computed: {
        fields() {
            return [
                { text: "Part Number", key: "part_number" },
                { text: "Type", key: "tipo" },
                { text: "Action", key: "action" }
            ]
        }
    },
    methods: {
        getItems() {
            const path = "http://localhost:8000/api/v1.0/items/"
            axios.get(path).then((response) => {
                this.items = response.data
            })
            .catch(() => {
                // console.log(error)
            })
        }
    },

    created() {
        this.getItems()
    },
}
</script>

<style lang="css" scoped>

</style>