<template>
  <b-container>
    <welcome-message></welcome-message>
    <transition name="fade" mode="out-in">
      <div v-if="currentPage == 'home'" key="homepage">
        <p class="instruction-text">
          What type of fault are we helping you with today?
          <br />If your handset has sustained physical damage to hardware,
          select
          <strong>Operational Fault.</strong>
          <br />For issues with handset functionality or behaviour, select
          <strong>Physical Fault.</strong>
        </p>
        <b-row class="menu-buttons-group">
          <button
            type="button"
            class="btn menu-button"
            v-on:click="currentPage = 'operationalSelected'"
          >
            <img
              class="button-icon"
              src="../assets/icons/icon-person-operation.png"
            />
            <p class="m-2 button-text">
              Operational
              <br />Fault
            </p>
          </button>
          <button
            type="button"
            class="btn menu-button"
            v-on:click="currentPage = 'physicalSelected'"
          >
            <img
              class="button-icon"
              src="../assets/icons/icon-person-handset.png"
            />
            <p class="m-2 button-text">
              Physical
              <br />Fault
            </p>
          </button>
          <button
            type="button"
            class="btn menu-button"
            @click="$router.push('howtoguides')"
          >
            <img class="button-icon" src="../assets/icons/icon-toolbox.png" />
            <p class="m-2 button-text">
              How-to
              <br />Guides
            </p>
          </button>
        </b-row>
      </div>
      <div v-if="currentPage == 'physicalSelected'" key="physicalfaults">
        <b-row class="menu-buttons-group">
          <button
            type="button"
            class="btn menu-button"
            v-on:click="currentPage = 'home'"
          >
            <img
              class="button-icon"
              src="../assets/icons/icon-person-handset.png"
            />
            <p class="m-2 button-text">
              Physical
              <br />Fault
            </p>
          </button>
        </b-row>
        <p class="instruction-text">
          If your handset has received significant physical damage,
          <br />please contact our team on <strong>123 456 789</strong> to
          organise a replacement with your Site ID, <br />required quantity,
          handset model, part number (if known), contact details and whether a
          quote is required.
        </p>
        <div class="nav-buttons">
          <b-btn class="btn back-button" v-on:click="backToPreviousPage"
            >Back</b-btn
          >
        </div>
      </div>
      <div v-if="currentPage == 'operationalSelected'" key="operationalfaults">
        <p class="instruction-text">
          If there is a functional issue with your handset, please tell us
          whether the operational fault is a
          <strong>single</strong> or
          <strong>multi-handset issue.</strong>
          <br />Or, if you have already confirmed the source of the problem
          yourself you can <strong>order a replacement handset or part</strong>.
          <br />If you have a different issue to report, please dial
          <strong>123 456</strong> and a member of our friendly staff will
          assist you.
        </p>
        <b-row class="menu-buttons-group">
          <button
            type="button"
            class="btn menu-button"
            v-on:click="currentPage = 'singleHandsetSelected'"
          >
            <img
              class="button-icon"
              src="../assets/icons/icon-single-person.png"
            />
            <p class="m-2 button-text">
              Single Handset
              <br />Issue
            </p>
          </button>
          <button
            type="button"
            class="btn menu-button"
            v-on:click="currentPage = 'multiHandsetSelected'"
          >
            <img
              class="button-icon"
              src="../assets/icons/icon-multiple-people.png"
            />
            <p class="m-2 button-text">
              Multi Handset
              <br />Issue
            </p>
          </button>
          <button
            type="button"
            class="btn menu-button"
            v-on:click="currentPage = 'orderReplacementSelected'"
          >
            <img
              class="button-icon"
              src="../assets/icons/icon-envelope-phone.png"
            />
            <p class="m-2 button-text">
              Order Replacement
              <br />Part
            </p>
          </button>
        </b-row>
        <div class="nav-buttons">
          <b-btn class="btn back-button" v-on:click="backToPreviousPage"
            >Back</b-btn
          >
        </div>
      </div>
      <div
        v-if="currentPage == 'singleHandsetSelected'"
        key="singlehandsetfaults"
      >
        <b-row class="menu-buttons-group">
          <button
            type="button"
            class="btn menu-button"
            v-on:click="currentPage = 'operationalSelected'"
          >
            <img
              class="button-icon"
              src="../assets/icons/icon-single-person.png"
            />
            <p class="m-2 button-text">
              Single Handset
              <br />Issue
            </p>
          </button>
        </b-row>
        <p class="instruction-text">
          If you have an isolated issue that affects only one device, please
          proceed
          <br />to the triage process where we will ask you a few questions
          about your issue.
        </p>
        <div class="nav-buttons">
          <b-btn class="btn back-button" v-on:click="backToPreviousPage"
            >Back</b-btn
          >
          <b-btn class="btn proceed-button" to="singlehandsettriage"
            >Proceed</b-btn
          >
        </div>
      </div>
      <div
        v-if="currentPage == 'multiHandsetSelected'"
        key="multihandsetfaults"
      >
        <b-row class="menu-buttons-group">
          <button
            type="button"
            class="btn menu-button"
            v-on:click="currentPage = 'operationalSelected'"
          >
            <img
              class="button-icon"
              src="../assets/icons/icon-multiple-people.png"
            />
            <p class="m-2 button-text">
              Multi Handset
              <br />Issue
            </p>
          </button>
        </b-row>
        <p class="instruction-text">
          If you have an issue that seems to affect multiple devices, please
          call
          <strong>123 456</strong>
          <br />with your
          <strong>SiteID, model and part number ready</strong> and our friendly
          staff will assist <br />in finding a solution for you.
        </p>
        <div class="nav-buttons">
          <b-btn class="btn back-button" v-on:click="backToPreviousPage"
            >Back</b-btn
          >
        </div>
      </div>
      <div
        v-if="currentPage == 'orderReplacementSelected'"
        key="orderreplacement"
      >
        <b-row class="menu-buttons-group">
          <button
            type="button"
            class="btn menu-button"
            v-on:click="currentPage = 'operationalSelected'"
          >
            <img
              class="button-icon"
              src="../assets/icons/icon-envelope-phone.png"
            />
            <p class="m-2 button-text">
              Order Replacement
              <br />Part
            </p>
          </button>
        </b-row>
        <p class="instruction-text">
          Proceed
          <strong>
            only if you have already identified the source of the problem
            <br />yourself
          </strong>
          and are in need of a replacement handset or part.
        </p>
        <div class="nav-buttons">
          <b-btn class="btn back-button" v-on:click="backToPreviousPage"
            >Back</b-btn
          >
          <b-btn class="btn proceed-button" to="orderreplacement"
            >Proceed</b-btn
          >
        </div>
      </div>
    </transition>
  </b-container>
</template>
<script>
import WelcomeMessage from "../components/WelcomeMessage.vue";

export default {
  data() {
    return {
      currentPage: "home"
    };
  },
  methods: {
    backToPreviousPage() {
      switch (this.currentPage) {
        case "physicalSelected":
        case "operationalSelected":
          this.currentPage = "home";
          return;
        case "singleHandsetSelected":
        case "multiHandsetSelected":
        case "orderReplacementSelected":
          this.currentPage = "operationalSelected";
          return;
      }
    }
  },
  components: {
    "welcome-message": WelcomeMessage
  }
};
</script>
<style>
.btn.menu-button {
  /* position: absolute; */
  width: 220px;
  height: 220px;
  background: none;
  border-color: white;
  border-width: 6px;
  border-radius: 100%;
  margin: auto;
  margin-top: 2%;
  margin-bottom: 2%;
}

.btn.menu-button:hover {
  border-color: white;
  background-color: #ffffff40;
}

.btn.menu-button:active {
  border-color: white;
  background-color: #ffffff17;
}

.btn.back-button {
  color: #a0fff5;
  background: none;
  border: none;
  bottom: 10%;
}

.btn.proceed-button {
  color: #a0fff5;
  background: none;
  border: none;
  bottom: 10%;
  right: 0px;
}

.btn.back-button:hover,
.btn.proceed-button:hover {
  color: #a0fff5;
  background-color: #ffffff40;
  border: none;
}

.btn.back-button:active,
.btn.proceed-button:active {
  color: #a0fff5;
  background-color: #ffffff10;
  border: none;
}

.btn.back-button:focus,
.btn.proceed-button:focus {
  border: none;
}

.instruction-text {
  color: white;
  text-align: center;
}

#div .menu-buttons-group {
  justify-content: center;
  width: 80%;
  margin: auto;
}

.menu-button .button-icon {
  width: 80px;
  height: 80px;
  background: transparent;
}

.menu-button .button-text {
  color: white;
}

.nav-buttons {
  text-align: center;
}

/* transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.7s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.menu-buttons-enter-active,
.menubutton-leave-active {
  transition: opacity 0.5s ease-out;
}

.menu-buttons-enter,
.menubutton-leave-to {
  opacity: 0;
}
</style>
