<template>
    <div class="triage-questions">
        <triage-crackle-noise  @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MITEL3300S1'"/>
        <triage-faded-keys @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MITEL3300S2'"/>
        <triage-hook-flash @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MITEL3300S3'"/>
        <triage-outgoing-calls-busy @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MITEL3300S4'"/>
        <triage-one-way-speech @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MITEL3300S5'"/>
        <triage-option-129 @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MITEL3300S6'"/>
        <triage-pixelated-display @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MITEL3300S7' || selectedSymptom=='MXONES11'"/>
        <triage-phone-not-ringing @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MITEL3300S8'"/>
        <triage-dead-phone @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MITEL3300S9'"/>
        <triage-dhcp-discovery @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MITEL3300S10'"/>
        <triage-mitel-3300 @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MITEL3300S11'"/>
        <mxmd-calls-drop-out @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MXONES1'"/>
        <mxmd-low-signal-strength @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MXONES2'"/>
        <mxmd-cant-log-in @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MXONES3'"/>
        <mxmd-crackle-noise @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MXONES4'"/>
        <mxmd-hook-flash @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MXONES5'"/>        
        <mxmd-one-way-speech @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MXONES6'"/>
        <mxmd-phone-doesnt-ring @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MXONES8'"/>
        <mxmd-dead-phone @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MXONES9'"/>
        <mxmd-phone-not-charging @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MXONES10'"/>
        <mxmd-keys-not-working @show-solution-modal="$bvModal.show($event)" v-if="selectedSymptom=='MXONES12'"/>

        <!-- 1 -->
        <b-modal id="sendEmailModal" size="lg" hide-footer hide-header> 
            <div class="d-block p-5 modal-body-text">
                <p>
                    Click <strong>Proceed</strong> below to continue to the Order Replacement Handset page, where you can send a request for a replacement handset to the faults Faults team.
                </p>
            </div>
            <b-button class="my-5 mx-auto modal-proceed-button" block to="/orderreplacement" > Proceed </b-button>             
            <b-button class="my-5 mx-auto modal-close-button" block @click="$bvModal.hide('sendEmailModal')"> Close </b-button>
        </b-modal>
        <!-- 2 -->
        <b-modal id="callMACTeamModal" size="lg" hide-footer hide-header> 
            <div class="d-block p-5 modal-body-text">
                <p>
                    Call our team on 123 456 789 and request a handset replacement, with the following information at hand: <br/><br/>
                    <ul>
                        <li>Site ID</li>
                        <li>Quantity</li>
                        <li>Model</li>
                        <li>Part Number (found on the white sticker on the back of the device)</li>
                        <li>Contact Name</li>
                        <li>Contact Number</li>
                        <li>Contact Email</li>
                    </ul>
                    If a quote is required, please send an email to mac@team.email.com with the details above.
                </p>
            </div> 
            <b-button class="my-5 mx-auto modal-close-button" block @click="$bvModal.hide('callMACTeamModal')"> Close </b-button>
        </b-modal>
        <!-- 3 -->
        <b-modal id="notCoveredModal" size="lg" hide-footer hide-header> 
            <div class="d-block p-5 modal-body-text">
                <p>Unfortunately this is NOT covered under warranty and therefore fees may apply.
                    Call our team on 123 456 789 and request a handset replacement, with the following information at hand: <br/><br/>
                    <ul>
                        <li>Site ID</li>
                        <li>Quantity</li>
                        <li>Model</li>
                        <li>Part Number (found on the white sticker on the back of the device)</li>
                        <li>Contact Name</li>
                        <li>Contact Number</li>
                        <li>Contact Email</li>
                        <li>Delivery Address</li>
                    </ul>
                    Alternatively, if a quote is required please send an email to mac@team.email.com and provide the information above.
                </p>
            </div> 
            <b-button class="my-5 mx-auto modal-close-button" block @click="$bvModal.hide('notCoveredModal')"> Close </b-button>
        </b-modal>
        <!-- 4 -->
        <b-modal id="multipleHandsetModal" size="lg" hide-footer hide-header> 
            <div class="d-block p-5 modal-body-text">
                <p>Call the faults team on 123 456 to report multiple handset issues, with the following information at hand: <br/><br/>
                    <ul>
                        <li>Site ID</li>
                        <li>Quantity</li>
                        <li>Model</li>
                        <li>Part Number (found on the white sticker on the back of the device)</li>
                        <li>Contact Name</li>
                        <li>Contact Number</li>
                        <li>Contact Email</li>
                        <li>Delivery Address</li>
                    </ul>
                    Alternatively, if a quote is required please send an email to mac@team.email.com and provide the information above.
                </p>
            </div> 
            <b-button class="my-5 mx-auto modal-close-button" block @click="$bvModal.hide('multipleHandsetModal')"> Close </b-button>
        </b-modal>
        <!-- 5 -->
        <b-modal id="callITHelpdeskModal" size="lg" hide-footer hide-header> 
            <div class="d-block p-5 modal-body-text">
                <p>Call your IT help desk and report a port connectivity issue or a wall socket configuration issue. If your IT support is unable to resolve the issue, call the faults team on 123 456.</p>
            </div> 
            <b-button class="my-5 mx-auto modal-close-button" block @click="$bvModal.hide('callITHelpdeskModal')"> Close </b-button>
        </b-modal>
        <!-- 6 -->
        <b-modal id="callServiceProviderModal" size="lg" hide-footer hide-header> 
            <div class="d-block p-5 modal-body-text">
                <p>Please call your service provider to report a line fault.</p>
            </div> 
            <b-button class="my-5 mx-auto modal-close-button" block @click="$bvModal.hide('callServiceProviderModal')"> Close </b-button>
        </b-modal>
        <!-- 7 -->
        <b-modal id="callLineFault" size="lg" hide-footer hide-header> 
            <div class="d-block p-5 modal-body-text">
                <p>Please call one of the following numbers based on your service to report a line fault: </p>
                <ul>
                    <li>ISDN/PSTN: Call 132 255</li>
                    <li>TIPT/SIP: Call 1800 287 289</li>
                </ul>
            </div> 
            <b-button class="my-5 mx-auto modal-close-button" block @click="$bvModal.hide('callLineFault')"> Close </b-button>
        </b-modal>
    </div>
</template>
<script>
import TriageCrackleNoise from "../components/MitelTriageScenarios/TriageCrackleNoise"
import TriageDeadPhone from "../components/MitelTriageScenarios/TriageDeadPhone"
import TriageDHCPDiscovery from "../components/MitelTriageScenarios/TriageDHCPDiscovery"
import TriageMitel3300 from "../components/MitelTriageScenarios/TriageMitel3300"
import TriageOneWaySpeech from "../components/MitelTriageScenarios/TriageOneWaySpeech"
import TriageOption129 from "../components/MitelTriageScenarios/TriageOption129"
import TriageOutgoingCallsBusy from "../components/MitelTriageScenarios/TriageOutgoingCallsBusy"
import TriagePhoneNotRinging from "../components/MitelTriageScenarios/TriagePhoneNotRinging"
import TriagePixelatedDisplay from "../components/MitelTriageScenarios/TriagePixelatedDisplay"
import TriageHookFlash from "../components/MitelTriageScenarios/TriageHookFlash"
import TriageFadedKeys from "../components/MitelTriageScenarios/TriageFadedKeys"
import MXMDDeadPhone from "../components/MXMDTriageScenarios/MXMDDeadPhone"
import MXMDOneWaySpeech from "../components/MXMDTriageScenarios/MXMDOneWaySpeech"
import MXMDCrackleNoise from "../components/MXMDTriageScenarios/MXMDCrackleNoise"
import MXMDHookFlash from "../components/MXMDTriageScenarios/MXMDHookFlash"
import MXMDKeysNotWorking from "../components/MXMDTriageScenarios/MXMDKeysNotWorking"
import MXMDPhoneNotCharging from "../components/MXMDTriageScenarios/MXMDPhoneNotCharging"
import MXMDPhoneDoesntRing from "../components/MXMDTriageScenarios/MXMDPhoneDoesntRing"
import MXMDLowSignalStrength from "../components/MXMDTriageScenarios/MXMDLowSignalStrength"
import MXMDCantLogin from "../components/MXMDTriageScenarios/MXMDCantLogIn"
import MXMDCallsDropOut from "../components/MXMDTriageScenarios/MXMDCallsDropOut"

export default {
    data() {
        return {
            
        }
    },
    props: {
        selectedSymptom: String
    },
    components: {
        "triage-crackle-noise": TriageCrackleNoise,
        "triage-dead-phone": TriageDeadPhone,
        "triage-dhcp-discovery": TriageDHCPDiscovery,
        "triage-mitel-3300": TriageMitel3300,
        "triage-one-way-speech": TriageOneWaySpeech,
        "triage-option-129": TriageOption129,
        "triage-outgoing-calls-busy": TriageOutgoingCallsBusy,
        "triage-phone-not-ringing": TriagePhoneNotRinging,
        "triage-pixelated-display": TriagePixelatedDisplay,
        "triage-hook-flash": TriageHookFlash,
        "triage-faded-keys": TriageFadedKeys,
        "mxmd-dead-phone": MXMDDeadPhone,
        "mxmd-one-way-speech": MXMDOneWaySpeech,
        "mxmd-crackle-noise": MXMDCrackleNoise,
        "mxmd-hook-flash": MXMDHookFlash,
        "mxmd-keys-not-working": MXMDKeysNotWorking,
        "mxmd-phone-not-charging": MXMDPhoneNotCharging,
        "mxmd-phone-doesnt-ring": MXMDPhoneDoesntRing,
        "mxmd-low-signal-strength": MXMDLowSignalStrength,
        "mxmd-cant-log-in": MXMDCantLogin,
        "mxmd-calls-drop-out": MXMDCallsDropOut
    }
}
</script>
<style scoped>
.triage-questions {
    margin: 5%;
    justify-content: center;
}
.modal-body-text {
    text-align: left;
}

.modal-close-button {
    width: 50%; 
    background-color: #576DC3;
}

.modal-proceed-button {
    width: 50%; 
    background-color: rgb(147, 169, 255);
}
</style>