<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <stuk-list></stuk-list>
  </div>
</template>

<script>
// @ is an alias to /src
import StukList from '@/components/StukList.vue'

export default {
  name: 'HomeView',
  components: {
    StukList
  }
}
</script>
