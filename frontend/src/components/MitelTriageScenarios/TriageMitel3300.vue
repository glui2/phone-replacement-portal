<template>
    <div style="text-align: left">
        <div class="triage-radio-question">
            <ul>
                <li>On your PC, close the 5550 App.</li>
                <li>Removed the power cord from the keypad.</li>
                <li>After 10 seconds, plug the power cord back into the keypad.</li>
                <li>Wait for 30 seconds.</li>
            </ul>
            <b-form-group label="Has the red LED light disappeared from the keypad?" style="text-align: center; margin: 5%;">
                <b-form-radio-group
                id="S11-Q1"
                v-model="hasRedLightDisappeared"
                :options="options"
                buttons
                @change.native="firstQuestionResult(hasRedLightDisappeared)"
                name="S11-first-question"
                />
            </b-form-group>
            <ul v-if="hasRedLightDisappeared=='Yes'">
                <li>On your PC, go to <strong>Start Menu > All Programs > Mitel</strong> from the taskbar.</li>
                <li>Select the 5550 IP Console.</li>
                <li>Select <strong>Tools</strong>.</li>
                <li>Select <strong>Configuration Wizard</strong>.</li>
                <li>Once the Configuration Wizard window opens, click <strong>Next</strong> for all subsequent windows.</li>
                <li>When prompted with the "5550 IP console registered successfully" message, click <strong>Finish</strong></li>
                <li>Start the 5550 App, and check if the console is back online.</li>
            </ul>
            <b-form-group v-if="hasRedLightDisappeared=='Yes'" label="Click proceed below if the problem persists." style="text-align: center; margin: 5%;">
                <b-button @click="$emit('show-solution-modal', 'sendEmailModal')">Proceed</b-button>
            </b-form-group>
            
        </div>
    </div>    
</template>
<script>
export default {
    data() {
        return {
            hasRedLightDisappeared: "",
            isConsoleOnline: "",
            options: [
                { text: 'Yes', value: 'Yes' },
                { text: 'No', value: 'No' }
            ],
        }
    },
    methods: {
        firstQuestionResult(selectedRadioButton){
            if(selectedRadioButton=="No"){
                this.$emit('show-solution-modal', 'sendEmailModal' )
            }
        },
    },
    
}
</script>
<style scoped>
.triage-radio-question { 
    color: white;     
    justify-content: center;
    margin: 3%;
}
</style>