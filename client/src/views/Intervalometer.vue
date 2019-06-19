<template>
  <v-container>
    <v-layout justify-center align-center>
      <v-flex>
        <v-text-field label="Exposures" type="number" v-model="count" min="1"></v-text-field>
        <v-select :disabled="useBulb" :items="speeds" label="Shutter Speed" v-model="speed"></v-select>
        <v-layout row>
          <v-flex xs3>
            <v-switch
              v-model="useBulb"
              label="Bulb"
            ></v-switch>
          </v-flex>
          <v-flex xs9>
            <v-text-field label="Time (s)" type="number" v-model="bulbSpeed" min="1"></v-text-field>
          </v-flex>
        </v-layout>
        <v-text-field label="Delay (s)" type="number" v-model="delay" min="0"></v-text-field>
        <v-btn color="success" @click="start">Start</v-btn>
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
      useBulb: false,
      bulbSpeed: 1,
      delay: 0,
      speeds: null
    };
  },
  methods: {
    start: function () {
      let data = {
        count: this.count,
        delay: this.delay,
        useBulb: this.useBulb,
        speed: this.useBulb ? this.bulbSpeed : this.speed
      };

      axios.post('/api/interval', data).then(response => {

      })
    }
  },
  mounted () {
    axios.get('/api/speeds')
      .then(response => {
        this.speeds = response.data;
      })
      .catch(error => {

      });
  }
};
</script>
