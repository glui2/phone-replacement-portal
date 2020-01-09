<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Has the phone been dropped or physically damaged?">
                <b-form-radio-group
                id="S16-Q1"
                v-model="hasPhysicalDamage"
                :options="options"
                buttons
                @change.native="damagedQuestionResult(hasPhysicalDamage)"
                name="S16-first-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="hasPhysicalDamage=='No'" class="triage-radio-question">
            <b-form-group label="Ensure the network cable is properly connected and click Proceed if the problem persists.">
                <b-button @click="didReconnectFix='No'">Proceed</b-button>
            </b-form-group>
        </b-row>
        <b-row v-if="hasPhysicalDamage=='No' && didReconnectFix=='No'" class="triage-radio-question">
            <b-form-group label="Disconnect and reconnect the cable and click Proceed if the problem persists.">
                <b-button @click="didDisconnectReconnectFix='No'">Proceed</b-button>
            </b-form-group>
        </b-row>
        <b-row v-if="hasPhysicalDamage=='No' && didReconnectFix=='No' && didDisconnectReconnectFix=='No'" class="triage-radio-question">
            <b-form-group label="Connect the phone to a known working phone port. Does this fix the issue?">
                <b-form-radio-group
                id="S16-Q4"
                v-model="worksOnOtherPort"
                :options="options"
                buttons
                @change.native="phonePortQuestionResult(worksOnOtherPort)"
                name="S16-fourth-question"/>
            </b-form-group>
        </b-row>               
    </div>
</template>
<script>
export default {
    data() {
        return {
            hasRattling: '',
            hasPhysicalDamage: '',
            didReconnectFix: '',
            didDisconnectReconnectFix: '',
            worksOnOtherPort: '',  
            options: [
                { text: 'Yes', value: 'Yes' },
                { text: 'No', value: 'No' }
            ]
        }
    },
    methods: {
        damagedQuestionResult(selectedRadioButton){
            if(selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'notCoveredModal' )
            }
        },

        phonePortQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "No"){
                this.$emit('show-solution-modal', 'sendEmailModal' )
            }
            else{
                this.$emit('show-solution-modal', 'callITHelpdeskModal')
            }
        }
    },
}
</script>
<style scoped>
.triage-radio-question { 
    color: white;     
    justify-content: center;
    margin: 3%;
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