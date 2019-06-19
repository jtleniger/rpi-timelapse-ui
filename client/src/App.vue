<template>
  <v-app dark>
    <v-navigation-drawer v-model="drawer" clipped fixed app>
      <v-list dense>
        <v-list-tile :to="'/'">
          <v-list-tile-action>
            <v-icon>timelapse</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Intervalometer</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile :to="'/bracketing'">
          <v-list-tile-action>
            <v-icon>tonality</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Bracketing</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-divider></v-divider>
        <v-list-tile>
          <v-list-tile-action>
            <v-icon>power_off</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Shutdown</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title class="headline text-uppercase">
        <span>RASPBERRY</span>
        <span class="font-weight-light">NIKON</span>
      </v-toolbar-title>
    </v-toolbar>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      drawer: false
    };
  }
};
</script>
