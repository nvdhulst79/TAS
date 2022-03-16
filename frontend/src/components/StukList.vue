<template>
  <div>
    <h4 v-if="loading">Loading...</h4>
    <stuk-item
      v-for="stuk in alleStukken"
      :key="stuk.id"
      :stuk="stuk">
    </stuk-item>
  </div>
</template>

<script>
/* eslint-disable */
import { ALLE_STUKKEN_QUERY } from '../constants/graphql'
import StukItem from './StukItem'

export default {
    name: 'StukList',
    data () {
        return {
            alleStukken: [],
            loading: 0
        }
    },
    components: {
        StukItem
    },
    apollo: {
        alleStukken: {
            query: ALLE_STUKKEN_QUERY
        }
    }
}
</script>
