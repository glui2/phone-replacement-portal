<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Check the port where the handset has been connected to. Has the connected port been configured by your IT team?">
                <b-form-radio-group
                id="S19-Q1"
                v-model="isPortConfigured"
                :options="options"
                buttons
                @change.native="firstQuestionResult(isPortConfigured)"
                name="S19-first-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="isPortConfigured=='Yes'" class="triage-radio-question">
            <b-form-group label="Connect the handset to another working port. Does this resolve the issue?">
                <b-form-radio-group
                id="S19-Q2"
                v-model="worksOnOtherPort"
                :options="options"
                buttons
                @change.native="secondQuestionResult(worksOnOtherPort)"
                name="S19-second-question"/>
            </b-form-group>
        </b-row>                  
    </div>
</template>
<script>
export default {
    data() {
        return {
            isPortConfigured: '',
            worksOnOtherPort: '',
            options: [
                { text: 'Yes', value: 'Yes' },
                { text: 'No', value: 'No' }
            ],
        }
    },
    methods: {
        firstQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "No"){
                this.$bvModal.show('callITHelpdeskModal'); 
            }
        },
        secondQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'callITHelpdeskModal')
            }
            else {
                this.$emit('show-solution-modal','sendEmailModal')
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

.modal-proceed-button-disabled {
    width: 50%; 
    background-color: grey;
}

#orderCurlyCordModal .handset-model-dropdown {
    text-align: center;
    width: 70%; 
}
</style>