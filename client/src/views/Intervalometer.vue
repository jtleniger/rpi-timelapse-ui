<template>
  <v-container>
    <v-layout justify-center align-center>
      <v-flex>
        <v-text-field label="Exposures" type="number" v-model="count" min="1"></v-text-field>
        <v-select :items="items" label="Shutter Speed" v-model="shutterSpeed"></v-select>
        <v-text-field label="Delay" type="number" v-model="delay" min="0"></v-text-field>
        <v-btn color="success">Start</v-btn>
        <v-btn color="error">Stop</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: function() {
    return {
      count: 1,
      shutterSpeed: "foo",
      delay: 0,
      items: ["foo", "bar"]
    };
  }
};
</script>
