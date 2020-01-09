<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Is the phone physically damaged or broken?">
                <b-form-radio-group
                id="S7-Q1"
                v-model="isPhysicallyBroken"
                :options="options"
                buttons
                @change.native="firstQuestionResult(isPhysicallyBroken)"
                name="S7-first-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="isPhysicallyBroken=='No'" class="triage-radio-question">
            <b-form-group label="Has liquid been spilled on the screen?">
                <b-form-radio-group
                id="S7-Q2"
                v-model="hasLiquidSpilledOnScreen"
                :options="options"
                buttons
                @change.native="secondQuestionResult(hasLiquidSpilledOnScreen)"
                name="S7-second-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="hasLiquidSpilledOnScreen=='No' && isPhysicallyBroken=='No'" class="triage-radio-question">
            <b-form-group label="Restart the phone if you haven't done so already. If this did not resolve the issue, click Proceed  and place a request for a replacement handset using the order form.">
                <b-button to="/orderreplacement">Proceed</b-button>
            </b-form-group>
        </b-row>                                           
    </div>
</template>
<script>
export default {
    data() {
        return {
            isPhysicallyBroken: '',
            hasLiquidSpilledOnScreen: '',
            hasPhoneRestarted: '',
            didRestartFail: '', 
            options: [
                { text: 'Yes', value: 'Yes' },
                { text: 'No', value: 'No' }
            ],
        }
    },
    methods: {
        firstQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'notCoveredModal' )
            }
        },
        secondQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'notCoveredModal' )
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