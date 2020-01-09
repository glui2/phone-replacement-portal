<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Is there any noticeable or physical damage to the handset?">
                <b-form-radio-group
                id="S3-Q1"
                v-model="hasPhysicalDamage"
                :options="options"
                buttons
                @change.native="firstQuestionResult(hasPhysicalDamage)"
                name="S3-first-question"/>
            </b-form-group>
        </b-row>      
    </div>
</template>
<script>
export default {
    data() {
        return {
            hasPhysicalDamage: '',
            options: [
                { text: 'Yes', value: 'Yes' },
                { text: 'No', value: 'No' }
            ]
        }
    },
    methods: {
        firstQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'notCoveredModal' )
            }
            else {
                this.$emit('show-solution-modal', 'sendEmailModal' )
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
</style>