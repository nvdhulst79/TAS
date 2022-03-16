<template>
  <div>
    <div class="flex flex-column mt3">
      <input
        class="mb2"
        v-model="titel"
        type="text"
        placeholder="De titel van het stuk">
      <input
        class="mb2"
        v-model="auteur"
        type="text"
        placeholder="De auteur">
    </div>
    <button @click="createStuk()">Opslaan</button>
  </div>
</template>

<script>
/* eslint-disable */
  import { CREATE_STUK_MUTATION } from '../constants/graphql'

  export default {
    name: 'CreateStuk',
    data () {
      return {
        titel: '',
        auteur: ''
      }
    },
    methods: {
      createStuk () {
        const { titel, auteur } = this.$data
        this.$apollo.mutate({
            mutation: CREATE_STUK_MUTATION,
            variables: {
                titel,
                auteur
            }
        })
      }
    }
  }
</script>