import * as Yup from 'yup';
export const loginSchema = Yup.object().shape({
    username: Yup.string().min(3, "Username must be at least 3 characters long").required("Please Enter Username"),
    password: Yup.string().required("Please Enter Valid Password")
});
