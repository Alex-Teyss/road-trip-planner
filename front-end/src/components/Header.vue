<script setup lang="ts"></script>

<template>
  <header>
    <nav class="bg-white border-gray-200 px-4 lg:px-6 py-2.5 dark:bg-gray-800">
      <div
        class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl"
      >
        <a href="">
          <img
            src="../assets/image.png"
            class="mr-3 h-6 sm:h-9"
            alt="Flowbite Logo"
          />
        </a>
        <div class="flex">
          <div class="flex items-center lg:order-2">
            <a
              href="#"
              class="text-gray-800 dark:text-white hover:bg-gray-50 focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 dark:hover:bg-gray-700 focus:outline-none dark:focus:ring-gray-800"
              ><svg
                width="23"
                height="22"
                viewBox="0 0 23 22"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M21.6445 21L16.9224 16.2695L21.6445 21ZM19.5393 9.94737C19.5393 12.3204 18.5966 14.5962 16.9186 16.2741C15.2407 17.9521 12.9649 18.8947 10.5919 18.8947C8.21891 18.8947 5.94311 17.9521 4.26516 16.2741C2.5872 14.5962 1.64453 12.3204 1.64453 9.94737C1.64453 7.57438 2.5872 5.29858 4.26516 3.62062C5.94311 1.94267 8.21891 1 10.5919 1C12.9649 1 15.2407 1.94267 16.9186 3.62062C18.5966 5.29858 19.5393 7.57438 19.5393 9.94737V9.94737Z"
                  stroke="#8A53FF"
                  stroke-width="2"
                  stroke-linecap="round"
                />
              </svg>
            </a>
            <a
              href="#"
              class="text-gray-800 hover:bg-gray-50 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800"
              ><svg
                width="25"
                height="24"
                viewBox="0 0 25 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M12.6445 5.14282C11.7969 5.14282 10.9683 5.39418 10.2635 5.8651C9.55874 6.33602 9.00943 7.00535 8.68506 7.78846C8.36068 8.57158 8.27581 9.43329 8.44118 10.2646C8.60654 11.096 9.01472 11.8596 9.61408 12.459C10.2135 13.0584 10.9771 13.4665 11.8084 13.6319C12.6398 13.7973 13.5015 13.7124 14.2846 13.388C15.0677 13.0636 15.7371 12.5143 16.208 11.8096C16.6789 11.1048 16.9303 10.2762 16.9303 9.42854C16.9303 8.29189 16.4787 7.20181 15.675 6.39808C14.8713 5.59435 13.7812 5.14282 12.6445 5.14282ZM12.6445 12C12.136 12 11.6388 11.8492 11.2159 11.5666C10.7931 11.284 10.4635 10.8824 10.2689 10.4126C10.0742 9.94271 10.0233 9.42568 10.1225 8.92688C10.2217 8.42807 10.4666 7.96988 10.8263 7.61026C11.1859 7.25064 11.6441 7.00574 12.1429 6.90652C12.6417 6.8073 13.1587 6.85822 13.6286 7.05285C14.0985 7.24747 14.5001 7.57706 14.7826 7.99993C15.0652 8.4228 15.216 8.91996 15.216 9.42854C15.2153 10.1103 14.9442 10.764 14.4621 11.2461C13.98 11.7281 13.3263 11.9993 12.6445 12Z"
                  fill="#8A53FF"
                />
                <path
                  d="M12.6445 0C10.2712 0 7.95108 0.703788 5.97769 2.02236C4.0043 3.34094 2.46623 5.21508 1.55798 7.4078C0.649731 9.60051 0.412091 12.0133 0.875113 14.3411C1.33814 16.6689 2.48102 18.807 4.15925 20.4853C5.83748 22.1635 7.97568 23.3064 10.3035 23.7694C12.6312 24.2324 15.044 23.9948 17.2367 23.0865C19.4294 22.1783 21.3036 20.6402 22.6222 18.6668C23.9407 16.6934 24.6445 14.3734 24.6445 12C24.6409 8.81851 23.3755 5.76838 21.1258 3.51873C18.8762 1.26908 15.826 0.00362976 12.6445 0ZM7.50168 20.8946V19.7143C7.50236 19.0325 7.7735 18.3788 8.25558 17.8968C8.73767 17.4147 9.39133 17.1435 10.0731 17.1429H15.216C15.8977 17.1435 16.5514 17.4147 17.0335 17.8968C17.5156 18.3788 17.7867 19.0325 17.7874 19.7143V20.8946C16.2267 21.8059 14.4518 22.2861 12.6445 22.2861C10.8372 22.2861 9.06239 21.8059 7.50168 20.8946ZM19.4948 19.6509C19.4777 18.5266 19.0197 17.454 18.2193 16.6642C17.419 15.8744 16.3404 15.4307 15.216 15.4286H10.0731C8.94869 15.4307 7.87011 15.8744 7.06975 16.6642C6.2694 17.454 5.81133 18.5266 5.79425 19.6509C4.23988 18.2629 3.14373 16.4356 2.65097 14.4109C2.1582 12.3861 2.29205 10.2594 3.0348 8.31245C3.77755 6.36546 5.09415 4.69 6.81028 3.50791C8.52641 2.32583 10.5611 1.69288 12.645 1.69288C14.7288 1.69288 16.7635 2.32583 18.4796 3.50791C20.1958 4.69 21.5124 6.36546 22.2551 8.31245C22.9979 10.2594 23.1317 12.3861 22.639 14.4109C22.1462 16.4356 21.05 18.2629 19.4957 19.6509H19.4948Z"
                  fill="#8A53FF"
                />
              </svg>
            </a>
            <button
              data-collapse-toggle="mobile-menu-2"
              type="button"
              class="inline-flex items-center p-2 ml-1 text-sm text-gray-500 rounded-lg lg:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
              aria-controls="mobile-menu-2"
              aria-expanded="false"
            >
              <span class="sr-only">Open main menu</span>
              <svg
                class="w-6 h-6"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <svg
                class="hidden w-6 h-6"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
            </button>
          </div>
          <div
            class="hidden justify-between items-center w-full lg:flex lg:w-auto lg:order-1"
            id="mobile-menu-2"
          >
            <ul
              class="flex flex-col mt-4 font-medium lg:flex-row lg:space-x-8 lg:mt-0 mr-4"
            >
              <li>
                <a
                  href="#"
                  class="block py-2 pr-4 pl-3 text-white rounded bg-primary-700 lg:bg-transparent lg:text-primary-700 lg:p-0 dark:text-white"
                  aria-current="page"
                  >Home</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700"
                  >Story</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700"
                  >Gallery</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700"
                  >Contact us</a
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<style scoped></style>
