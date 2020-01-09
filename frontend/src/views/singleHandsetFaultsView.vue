<template>
  <b-container>
    <transition>
      <h5 class="h5 please-tell-us">
        Please tell us about your faulty handset.
      </h5>
    </transition>
    <div class="m-4">
      <transition>
        <b-row>
          <b-col class="px-4 handset-model-instruction"
            >Please select your handset model from below:</b-col
          >
          <b-col class="px-4 handset-model-help">
            <b-button
              v-b-modal.handsetModelHelpModal
              class="handset-model-help-link"
              variant="link"
              >How can I find my handset model?</b-button
            >
          </b-col>
        </b-row>
      </transition>
      <b-modal id="handsetModelHelpModal" size="lg" hide-footer hide-header>
        <div class="d-block p-5 modal-body-text">
          <p>
            You can usually locate the part number by turning the handset over
            and locating a white sticker with black text on the back of the
            handset. <br /><br />If your handset is not part of any of the
            series listed, please give our friendly staff a call on 123 456 and
            we'll assist you.
          </p>
        </div>
        <b-button
          class="my-5 mx-auto modal-close-button"
          block
          @click="$bvModal.hide('handsetModelHelpModal')"
        >
          Close
        </b-button>
      </b-modal>
      <transition>
        <b-form-select
          class="handset-model-dropdown my-2"
          v-model="selectedHandsetType"
          :options="handsetOptions"
        ></b-form-select>
        <!-- <symptoms-dropdown v-if="selectedHandsetType" :handsetType="selectedHandsetType"/>  -->
      </transition>
      <div v-if="selectedHandsetType" class="select-symptom-dropdown">
        <transition>
          <b-row>
            <b-col class="px-4 handset-model-instruction"
              >Please select the option which best matches your handset
              symptoms:</b-col
            >
            <b-col class="px-4 handset-model-help">
              <b-button
                v-b-modal.symptomHelpModal
                class="handset-model-help-link"
                variant="link"
                >What if my symptom does not fall under these
                categories?</b-button
              >
            </b-col>
          </b-row>
        </transition>
        <b-modal id="symptomHelpModal" size="lg" hide-footer hide-header>
          <div class="d-block p-5 modal-body-text">
            <p>
              You can give our friendly staff a call on 123 456, and we can
              determine an appropriate solution for your handset symptoms.
            </p>
          </div>
          <b-button
            class="my-5 mx-auto modal-close-button"
            block
            @click="$bvModal.hide('symptomHelpModal')"
          >
            Close
          </b-button>
        </b-modal>
        <transition>
          <b-form-select
            class="handset-symptom-dropdown my-2"
            v-model="selectedHandsetSymptom"
            :options="selectedSymptomOptions"
          ></b-form-select>
        </transition>
        <triage :selectedSymptom="selectedHandsetSymptom"></triage>
      </div>
      <div class="nav-buttons">
        <b-btn class="btn back-button" @click="$router.go(-1)">Back</b-btn>
      </div>
    </div>
  </b-container>
</template>
<script>
import symptoms from "../data/symptoms.json";
import handsets from "../data/handsets.json";
import Triage from "../components/Triage.vue";

export default {
  data() {
    return {
      handsetOptions: handsets,
      selectedHandsetType: null,
      symptomOptions: symptoms,
      selectedHandsetSymptom: null
    };
  },
  computed: {
    selectedSymptomOptions() {
      let model = this.selectedHandsetType;
      if (
        model == "MITEL330052" ||
        model == "MITEL330053" ||
        model == "MITEL330056" ||
        model == "MITEL330069"
      ) {
        model = model.slice(0, -2);
      }

      return this.symptomOptions["handsetType"][model];
    }
  },
  components: {
    triage: Triage
  }
};
</script>
<style>
.btn.back-button {
  color: #a0fff5;
  background: none;
  border: none;
  bottom: 10%;
}

.btn.handset-model-help-link {
  font-size: 15px;
  color: #a0fff5;
  text-align: right;
}

.btn.handset-model-help-link:hover {
  color: azure;
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

.handset-model-dropdown {
  text-align: center;
  padding-left: 20%;
  padding-right: 20%;
}

.handset-model-help {
  text-align: right;
}

.handset-model-instruction {
  text-align: left;
  font-size: 15px;
  color: white;
  align-self: center;
}

#handsetModelHelpModal .modal-body-text {
  text-align: left;
}

#handsetModelHelpModal .modal-close-button {
  width: 50%;
  background-color: #576dc3;
}

.nav-buttons {
  bottom: 0px;
  text-align: center;
}

#symptomHelpModal .modal-body-text {
  text-align: left;
}

#symptomHelpModal .modal-close-button {
  width: 50%;
  background-color: #576dc3;
}

.handset-symptom-dropdown {
  text-align: center;
}

.please-tell-us {
  color: white;
  text-align: center;
  margin: 40px;
}

.select-symptom-dropdown {
  margin-top: 5%;
  margin-bottom: 5%;
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
