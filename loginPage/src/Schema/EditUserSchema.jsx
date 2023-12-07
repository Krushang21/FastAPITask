import * as Yup from "yup";
export const EditUserSchema = Yup.object().shape({
  username: Yup.string()
    .trim()
    .min(3, "Username must be at least 3 characters long")
    .required("Please Enter Username"),
  email: Yup.string()
    .email("Invalid email address")
    .required("Email is required"),
});
