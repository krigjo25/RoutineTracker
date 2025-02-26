<template>

    <main>
        <Counter :data = RoutingTracker.Click />
    </main>
</template>

<script setup>

//  Importing necessary dependencies
import axios from 'axios';
import { reactive, ref, onMounted } from 'vue';

//  Importing components
import Counter from '../components/Counter.vue';

const RoutingTracker = reactive(
    {
        data: null
    }
);
const Response = async () => {

    await axios.get('http://localhost:5000').then((response) => {
        console.log(response.data);
        RoutingTracker.data = response.data;

    
    }).catch((error) => {
        console.log(error);
    });
}
onMounted(Response);

</script>