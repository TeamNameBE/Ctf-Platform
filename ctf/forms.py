import django.forms as forms
from ctf.models import Challenge, CTF


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, HTML


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ["name", "points", "description", "category", "pad"]


class CTForm(forms.ModelForm):
    class Meta:
        model = CTF
        fields = ["name", "start_date", "end_date", "website", "rating"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-form-ctf"
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            Fieldset(
                "",
                Field(
                    "name",
                    css_class="bg-white appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:border-blue-500",
                    placeholder="Ex: PlaidCTF",
                ),
                Field(
                    "start_date",
                    css_class="bg-white appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:border-blue-500",
                ),
                Field(
                    "end_date",
                    css_class="bg-white appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:border-blue-500"
                ),
                Field(
                    "website",
                    css_class="bg-white appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:border-blue-500"
                ),
                Field(
                    "rating",
                    css_class="bg-white appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:border-blue-500"
                ),
                HTML("""
                    <div class="mt-8 text-right">
                        <button type="button" class="bg-white hover:bg-gray-100 text-gray-700 font-semibold py-2 px-4 border border-gray-300 rounded-lg shadow-sm mr-2" @click="openEventModal = !openEventModal">
                            Cancel
                        </button>
                        <button type="submit" class="bg-gray-800 hover:bg-gray-700 text-white font-semibold py-2 px-4 border border-gray-700 rounded-lg shadow-sm" @click="addEvent()">
                            Save Event
                        </button>
                    </div>
                """)
            ),
        )
