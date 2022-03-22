<template>
  <div>
    <h2>Stuklist present</h2>
    <div v-if="loading">Loading...</div>
    <stuk-item
      v-for="stuk of result.alleStukken"
      :key="stuk.id"
      :stuk="stuk">
      stukstuk
    </stuk-item>
  </div>
</template>

<script>
import { ALLE_STUKKEN_QUERY } from '../constants/graphql'

import { useQuery } from '@vue/apollo-composable'
import StukItem from './StukItem.vue'
export default {
  setup(){
    const {result, loading} = useQuery(ALLE_STUKKEN_QUERY)
    
    
    return {
      result,
      loading,
    }

  },
  components: { StukItem}
}
</script>
