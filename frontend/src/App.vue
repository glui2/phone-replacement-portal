<template>
  <div>
    <b-navbar toggleable="lg" variant="white">
      <b-navbar-nav class="mr-auto">
        <b-nav-item href="#" class="h6 my-auto" to="/"
          >Handset Replacement &amp; Triage Portal</b-nav-item
        >
      </b-navbar-nav>
      <b-navbar-nav class="mx-auto">
        <b-nav-item href="#" disabled> </b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <b-nav-item
          href="#"
          class="h6 my-auto"
          style="width:333px; text-align:right"
          @click="$bvModal.show('logOutModal')"
          >Log Out</b-nav-item
        >
      </b-navbar-nav>
      <b-modal id="logOutModal" size="lg" hide-footer hide-header>
        <div class="d-block p-4 modal-body-text">
          <p class="my-auto">Are you sure you would like to log out?</p>
        </div>
        <div class="row">
          <b-button
            class="my-3 mx-auto modal-close-button"
            @click="$bvModal.hide('logOutModal')"
            >Yes</b-button
          >
          <b-button
            class="my-3 mx-auto modal-close-button"
            @click="$bvModal.hide('logOutModal')"
            >No</b-button
          >
        </div>
      </b-modal>
    </b-navbar>
    <transition name="fade-view" mode="out-in">
      <router-view />
    </transition>
  </div>
</template>
<style>
#app {
  margin: 5px;
}

body {
  background-image: url(./assets/background-blue.png);
  background-size: cover;
}

b-navbar {
  color: var(--primary);
}

#logOutModal .modal-body-text {
  text-align: center;
}

#logOutModal .modal-close-button {
  width: 30%;
}

/* Transitions */
.fade-view-enter-active,
.fade-view-leave-active {
  transition: opacity 1s;
}

.fade-view-enter,
.fade-view-leave-to {
  opacity: 0;
}
</style>
