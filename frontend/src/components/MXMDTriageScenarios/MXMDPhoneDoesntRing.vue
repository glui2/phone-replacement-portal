<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Has the phone been dropped or physically damaged?">
                <b-form-radio-group
                id="S19-Q1"
                v-model="hasPhysicalDamage"
                :options="options"
                buttons
                @change.native="firstQuestionResult(hasPhysicalDamage)"
                name="S19-first-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="hasPhysicalDamage=='No'" class="triage-radio-question">
            <b-form-group label="Check that the volume has been set correctly, and click Proceed if the problem persists.">
                <b-button @click="didVolumeFix='No'">Proceed</b-button>
            </b-form-group>
        </b-row>
        <b-row v-if="hasPhysicalDamage=='No' && didVolumeFix=='No'" class="triage-radio-question">
            <b-form-group label="Connect the handset to another port. Does this resolve the issue?">
                <b-form-radio-group
                id="S19-Q3"
                v-model="worksOnOtherPort"
                :options="options"
                buttons
                @change.native="thirdQuestionResult(worksOnOtherPort)"
                name="S19-third-question"/>
            </b-form-group>
        </b-row>                           
    </div>
</template>
<script>
export default {
    data() {
        return {
            hasPhysicalDamage: '',
            didVolumeFix: '',
            worksOnOtherPort: '',
            options: [
                { text: 'Yes', value: 'Yes' },
                { text: 'No', value: 'No' }
            ]
        }
    },
    methods: {
        firstQuestionResult(selectedRadioButton){
            if(selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'notCoveredModal' )
            }
        },
        thirdQuestionResult(selectedRadioButton){
            if(selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'sendEmailModal' )
            }
            else {
                 this.$emit('show-solution-modal', 'callITHelpdeskModal' )               
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

.modal-close-button {
    width: 50%; 
    background-color: #576DC3;
}

.modal-proceed-button {
    width: 50%; 
    background-color: rgb(147, 169, 255);
}
</style>