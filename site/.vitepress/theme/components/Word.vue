<script setup lang="ts">
// The wordmark as text: "sm" in ink, "alt" in smalt, the suffix in the product's text colour.
defineProps<{ product: string }>()
</script>

<template>
  <span class="sw-word">sm<span class="sw-alt">alt</span><span :class="`sw-sfx-${product}`">{{ product }}</span></span>
</template>
