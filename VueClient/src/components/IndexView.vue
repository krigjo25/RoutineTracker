<template>
  <div class="greetings">

      <h1>Score: <span id="score">{{ count }}</span></h1>
        <form>
            <button @click="updateClicks">Click me to increase score</button>
            <button type="reset">Reset Button</button>
        </form>
  </div>
</template>

<script setup>
//  Importing required dependencies
import axios from 'axios'
import { onMounted, ref } from 'vue'

const count = ref(0)
const Response = async () => 
{
  const path = 'http://localhost:5000/'
  await axios.get(path).then((response) => 
  {
    count.value = response.data.count
  }).catch((error) => 
  {
    console.log(error)
  })
}

async function updateClicks()
  {
    const path = "http://localhost:5000/"
    await axios.post(path, {"count": count.value += 1}).then(
      (response) => 
    {
      Response()
    }).catch((error) => 
    {
      console.log(error)
    })
  }



onMounted(Response);



</script>