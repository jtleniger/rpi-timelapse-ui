<template>
  <v-container>
    <v-layout justify-center align-center>
      <v-flex>
        <v-text-field label="Exposures" type="number" v-model="count" min="1" step="2"></v-text-field>
        <v-text-field label="Step (stops)" type="number" v-model="step" min="1"></v-text-field>
        <v-btn color="success">Start</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
    data: function () {
        return {
            count: 1,
            step: 1
        }
    }
}
</script>
