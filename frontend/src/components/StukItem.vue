<template>
  <div>
      <h3>Item present!</h3>
      <b>{{stuk.titel}}</b><br/>
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
