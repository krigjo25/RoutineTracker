<template>
    <section>
        <h1>Current Routine: {{ RoutineData}}</h1>
        <button @click="UpdateCookie">Increment</button>
    </section>
</template>
<script setup>

//  Importing necessary dependencies
import { ref, reactive, defineProps } from 'vue';

//  Defining props
const props = defineProps(
    {
        data: {
            default: 0,
            type: Number,
            required: true,
        },
    }
)
const RoutineData = ref(props.data);


function increment()
{
    //  Incrementing the counter
    RoutineData.value++;
}
function UpdateCookie() {

    //  Incrementing the counter
    increment();

    //  Sending the updated counter to the server
    axios.put('http://localhost:5000', {
        data: RoutineData.value}).then((response) => {
        console.log(response.data);
    }).catch((error) => {
        console.log(error);
    });
}

</script>