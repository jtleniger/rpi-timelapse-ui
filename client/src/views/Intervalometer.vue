<template>
  <v-container>
    <v-layout justify-center align-center>
      <v-flex>
        <v-text-field label="Exposures" type="number" v-model="count" min="1"></v-text-field>
        <v-select :items="speeds" label="Shutter Speed" v-model="speed"></v-select>
        <v-text-field label="Delay" type="number" v-model="delay" min="0"></v-text-field>
        <v-btn color="success">Start</v-btn>
        <v-btn color="error">Stop</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data: function() {
    return {
      count: 1,
      speed: null,
      delay: 0,
      speeds: null
    };
  },
  mounted () {
    axios.get('/api/speeds')
      .then(response =>{
        this.speeds = response.data;
        this.speed = this.speeds[0];
      })
      .catch(error => {

      });
  }
};
</script>
