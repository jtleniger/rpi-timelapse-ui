<template>
  <q-layout view="hHr lpr fFf">

    <q-header bordered class="bg-negative text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-icon name="photo_camera"/>
          RaspberryNikon
        </q-toolbar-title>

        <q-btn dense flat round icon="menu" @click="right = !right" />
      </q-toolbar>

      <q-tabs>
        <q-route-tab to="/" label="Intervalometer" />
        <q-route-tab to="/bracketing" label="Bracketing" />
      </q-tabs>
    </q-header>

    <q-drawer v-model="right" side="right" behavior="mobile" bordered>
      <div class="q-pa-sm">
        <div class="row q-mt-md">
          <div class="col">
            <span class="text-subtitle1">Status:</span>
          </div>
        </div>
        <div class="row q-mt-md">
          <div class="col">
            <q-btn outline class="full-width" color="secondary" icon="power_off" label="Shutdown"/>
          </div>
        </div>
        <div class="row q-mt-md">
          <div class="col">
            <q-btn outline class="full-width" color="primary" icon="refresh" label="Reconnect"/>
          </div>
        </div>
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
export default {
  data () {
    return {
      right: true
    }
  }
}
</script>