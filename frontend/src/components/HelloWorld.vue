<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      Dit is het begin van een mooie frontend voor TAS. We gebruiken 
      <a target="_blank" href="https://vitejs.dev/">Vite</a> +
      <a target="_blank" href="https://vuejs.org/">Vue 3</a> +
      <a target="_blank" href="https://v4.apollo.vuejs.org">Apollo 4</a>.
    </h3>
    <h3>
      Het backend draait op
      <a target="_blank" href="https://www.djangoproject.com/">Django</a> +
      <a target="_blank" href="https://docs.graphene-python.org/projects/django/en/latest/">Graphene</a>.
    </h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
