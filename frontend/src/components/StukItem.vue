<template>
  <div>
      <b>{{stuk.titel}}</b><br/>
      {{stuk.auteur}}<br/>
      {{stuk.genre.naam}} ({{stuk.genre.omschrijving}})
  </div>
</template>

<script>
/* eslint-disable */
export default {
    name: 'StukItem',
    props: ['stuk']
}
</script>
